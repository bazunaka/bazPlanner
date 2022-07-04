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

        static public int CheckAuth()
        {
            command = new SQLiteCommand(connection)
            {
                 CommandText = "SELECT * FROM owner"
            };
            int cnt = command.ExecuteReader().StepCount;
            Console.WriteLine(cnt);
            return cnt;
        }

        static public string InsertUser(string nameUser, string passwordUser)
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"INSERT INTO owner (name_owner, password_owner) VALUES ('{nameUser}', '{passwordUser}')"
            };
            
            command.ExecuteNonQuery();
            string result = command.CommandText;
            Console.WriteLine(result);
            return result;
        }

        static public int CheckAdmin()
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = "SELECT * FROM owner WHERE name_owner='admin'"
            };
            int cnt = command.ExecuteReader().StepCount;
            Console.WriteLine(cnt);
            return cnt;
        }
    }
}
