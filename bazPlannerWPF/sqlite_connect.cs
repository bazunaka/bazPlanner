using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SQLite;

namespace bazPlannerWPF
{
    class sqlite_connect
    {
        static SQLiteConnection connection;
        static SQLiteCommand command;

        static public bool Connect(String fileName)
        {
            try
            {
                connection = new SQLiteConnection("Data Source=" + fileName + ";Version=3; FailIfMissing=False");
                connection.Open();
                return true;
            }
            catch (SQLiteException ex)
            {
                Console.WriteLine($"Ошибка доступа к базе данных. Исключение: {ex.Message}");
                return false;
            }
        }

        static public void CheckAuth()
        {
            if (Connect("test.db"))
            {
                command = new SQLiteCommand(connection)
                {
                    CommandText = "SELECT * FROM task"
                };
                int c = command.ExecuteReader().StepCount;

                Console.WriteLine(c);
            }

            else
            {
                Console.WriteLine("Error!!!");
            }
        }

    }
}
