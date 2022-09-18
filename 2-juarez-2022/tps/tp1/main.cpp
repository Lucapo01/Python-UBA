#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

const string csv_file_name = "libros.csv";
const int STEPS = 10;

const int GENRES_QTY = 6;
const int MIN_RATE_QTY = 3;
const int MAX_RATE = 100;

const string GENRES[GENRES_QTY] = {"Aventura", "Ciencia Ficcion", "Didactica", "Policiaca", "Romance", "Terror"};
const string GENRES_LETTERS[GENRES_QTY] = {"A", "C", "D", "P", "R", "T"};

struct Book
{
    string name;
    string genre;
    int rate;
};

void show_genres()
{
    cout << "Avilable genres are:" << endl;
    cout << "Aventura -> A" << endl;
    cout << "Ciencia Ficcion -> C" << endl;
    cout << "Didactica -> D" << endl;
    cout << "Policiaca -> P" << endl;
    cout << "Romance -> R" << endl;
    cout << "Terror -> T" << endl;
}

string letter_to_genre(string key)
{
    string genre = "Undefined genre";
    if (key == "A")
    {
        genre = "Aventura";
    }
    else if (key == "C")
    {
        genre = "Ciencia Ficcion";
    }
    else if (key == "D")
    {
        genre = "Didactica";
    }
    else if (key == "P")
    {
        genre = "Policiaca";
    }
    else if (key == "R")
    {
        genre = "Romance";
    }
    else if (key == "T")
    {
        genre = "Terror";
    }
    return genre;
}

void resize_vector(Book *&books, int &size)
{
    int new_size = size + STEPS;
    Book *new_books = new Book[new_size];

    for (int j = 0; j < size; j++)
    {
        new_books[j].name = books[j].name;
        new_books[j].genre = books[j].genre;
        new_books[j].rate = books[j].rate;
    }

    size = new_size;
    delete[] books;
    books = new_books;
}

void load(Book *&books, int &size, int &last)
{
    ifstream ip(csv_file_name);

    if (!ip.is_open())
        cout << "ERROR: File Open" << endl;

    string name;
    string genre;
    string rate_raw;
    int rate;

    int current_line = 0;
    while (ip.good())
    {
        getline(ip, name, ',');
        getline(ip, genre, ',');
        getline(ip, rate_raw, '\n');
        rate = stoi(rate_raw);

        // cout << "Name: " << name << endl;
        // cout << "Genre: " << genre << endl;
        // cout << "Rate: " << rate << endl;
        // cout << "-------------------" << endl;
        // cout << current_line << endl;

        books[current_line].name = name;
        books[current_line].genre = genre;
        books[current_line].rate = rate;

        current_line++;

        if (current_line == size - 1)
        {
            resize_vector(books, size);
        }
    }
    last = current_line;
    ip.close();
}

void show(Book *books, int size)
{
    cout << endl;
    for (int i = 0; i < size; i++)
    {
        cout << "pos: " << i << " - " << books[i].name << " - " << letter_to_genre(books[i].genre) << " - " << books[i].rate << endl;
    }
    cout << endl;
}

void add_book(Book *&books, int &size, int &last)
{
    string name;
    string genre;
    int rate;
    bool exists = false;

    cout << "Type book's name: ";
    cin >> name;

    for (int j = 0; j < last; j++)
    {
        if (books[j].name == name && exists == false)
        {
            cout << "That book already exists!" << endl;
            exists = true;
        }
    }

    if (!exists)
    {
        show_genres();
        cout << "Type book's genre LETTER: ";
        cin >> genre;
        cout << "Type book's rate: ";
        cin >> rate;

        if (last == size - 1)
        {
            resize_vector(books, size);
        }
        books[last].name = name;
        books[last].genre = genre;
        books[last].rate = rate;
        last++;
    }
}

void edit_rate(Book *&books, int last)
{
    string name;
    int rate;
    int book_to_edit_index = -1;

    cout << "Type book's name: ";
    cin >> name;

    for (int j = 0; j < last; j++)
    {
        if (books[j].name == name && book_to_edit_index == -1)
        {
            book_to_edit_index = j;
        }
    }

    if (book_to_edit_index != -1)
    {
        cout << "Type book's new rate: ";
        cin >> rate;
        books[book_to_edit_index].rate = rate;
    }
    else
    {
        cout << "That book name does not exist!" << endl;
    }
}

void fav_book(Book *books, int last)
{
    int max_rate = 0;
    string ties_arr[last];
    int ties_last = 0;

    for (int j = 0; j < last; j++)
    {
        if (books[j].rate > max_rate)
        {
            max_rate = books[j].rate;
            ties_arr[0] = books[j].name;

            for (int i = 1; i < ties_last; i++)
            {
                ties_arr[i] = "";
            }
            ties_last = 1;
        }

        else if (books[j].rate == max_rate)
        {
            ties_arr[ties_last] = books[j].name;
            ties_last++;
        }
    }

    cout << "Your Favorite/s Book/s: " << endl;
    for (int i = 0; i < ties_last; i++)
    {
        cout << ties_arr[i] << endl;
    }
}

void min_rate(Book *books, int last)
{
    {
        int firstmin = MAX_RATE + 1, secmin = MAX_RATE + 1, thirdmin = MAX_RATE + 1;
        string min_names[MIN_RATE_QTY];
        for (int i = 0; i < last; i++)
        {
            /* Check if current element is less than
               firstmin, then update first, second and
               third */
            if (books[i].rate < firstmin)
            {
                thirdmin = secmin;
                min_names[2] = min_names[1];
                secmin = firstmin;
                min_names[1] = min_names[0];
                firstmin = books[i].rate;
                min_names[0] = books[i].name;
            }

            /* Check if current element is less than
            secmin then update second and third */
            else if (books[i].rate < secmin)
            {
                thirdmin = secmin;
                min_names[2] = min_names[1];
                secmin = books[i].rate;
                min_names[1] = books[i].name;
            }

            /* Check if current element is less than
            then update third */
            else if (books[i].rate < thirdmin)
            {
                thirdmin = books[i].rate;
                min_names[2] = books[i].name;
            }
        }

        for (int i = 0; i < last; i++)
        {
            if (books[i].rate == thirdmin)
            {
                if (min_names[2].compare(books[i].name) > 0) // if first string is grater than second string, pick second
                {
                    if (books[i].name != min_names[0] && books[i].name != min_names[1])
                    {
                        min_names[2] = books[i].name;
                    }
                }
            }
        }

        cout << "These are your " << MIN_RATE_QTY << " least favorites books:" << endl;
        cout << " - " << min_names[0] << endl;
        cout << " - " << min_names[1] << endl;
        cout << " - " << min_names[2] << endl;
    }
}

void most_read_genre(Book *books, int last)
{
    int genres_read[GENRES_QTY];
    for (int j = 0; j < GENRES_QTY; j++)
    {
        genres_read[j] = 0;
    }
    int max_read_genre_qty = 0;
    for (int i = 0; i < last; i++)
    {
        for (int j = 0; j < GENRES_QTY; j++)
        {
            if (books[i].genre == GENRES_LETTERS[j])
            {
                genres_read[j]++;
                if (genres_read[j] > max_read_genre_qty)
                {
                    max_read_genre_qty = genres_read[j];
                }
            }
        }
    }
    cout << "Your most read genres are: " << endl;
    for (int j = 0; j < GENRES_QTY; j++)
    {
        if (genres_read[j] == max_read_genre_qty)
        {
            cout << GENRES[j] << endl;
        }
    }
}
void fav_genre(Book *books, int last)
{
    int genres_read[GENRES_QTY];
    int genres_rate_total[GENRES_QTY];
    float average[GENRES_QTY];
    float max_average = 0.0;

    // init to 0
    for (int j = 0; j < GENRES_QTY; j++)
    {
        genres_read[j] = 0;
        genres_rate_total[j] = 0;
    }

    // sum all the rates of a genre in genres_rate_total and add 1 by 1 the genres you read
    for (int i = 0; i < last; i++)
    {
        for (int j = 0; j < GENRES_QTY; j++)
        {
            if (books[i].genre == GENRES_LETTERS[j])
            {
                genres_rate_total[j] += books[i].rate;
                genres_read[j]++;
            }
        }
    }

    // average = total / quantity of genre read
    for (int j = 0; j < GENRES_QTY; j++)
    {
        average[j] = (float)genres_rate_total[j] / (float)genres_read[j];
        if (average[j] > max_average)
        {
            max_average = average[j];
        }
    }

    // print the max average genre
    cout << "Your favorite genres are: " << endl;
    for (int j = 0; j < GENRES_QTY; j++)
    {
        if (average[j] == max_average)
        {
            cout << GENRES[j] << " - avg: " << average[j] << endl;
        }
    }
}

int main()
{
    int size = STEPS;
    int last = 0;
    Book *books = nullptr;
    books = new Book[size];
    load(books, size, last);

    // add_book(books, size, last);
    // add_book(books, size, last);
    // add_book(books, size, last);
    show(books, last);

    // edit_rate(books, last);
    // fav_book(books, last);
    // min_rate(books, last);
    // most_read_genre(books, last);
    fav_genre(books, last);

    // cout << "Size: " << size << endl;

    delete[] books;
}