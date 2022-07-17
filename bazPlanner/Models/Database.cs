using System;
using System.Windows;
using System.Data.SQLite;
using System.Diagnostics;

namespace bazPlanner.Models
{
    class Database
    {
        public static SQLiteConnection? connection;
        public static SQLiteCommand? command;
        //Create connection. 
        static public bool Connect()
        {
            try
            {
                connection = new SQLiteConnection("Data Source=test.db; Version=3; FailIfMissing=False");
                connection.Open();
                Debug.WriteLine("Connected!");
                return true;
            }
            catch (SQLiteException ex)
            {
                Debug.WriteLine($"Ошибка доступа к базе данных. Исключение: {ex.Message}");
                return false;
            }
            
        }
        
        //Select owner for auth.
        static public int SelectOwner(string OwnerName, string OwnerPass)
        {
            string nameLower = OwnerName.ToLower();
            string passLower = OwnerPass.ToLower(); 
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT * FROM Owners WHERE OwnerName = '{nameLower}' AND OwnerPass = '{passLower}'"
            };
            int cnt = command.ExecuteReader().StepCount;
            return cnt;
        }

        //Select projects.
        static public bool SelectProjects(string OwnerName)
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT Projects.ProjectName FROM Projects INNER JOIN Owners ON Projects.ProjectOwner = Owners.OwnerID WHERE Owners.OwnerName = '{OwnerName}'"
            };
            SQLiteDataReader reader = command.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    ((MainWindow)Application.Current.MainWindow).listProjects.Items.Add(reader[0].ToString());
                }
            }
            return true;
        }

        //Insert project in database.
        static public bool InsertProject()
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"INSERT INTO Projects(ProjectName, ProjectOwner, ProjectDate) VALUES('project2-5', '2', '{DateTime.Now.ToShortDateString}')"
            };
            int result = command.ExecuteNonQuery();
            if (result == 0)
            {
                Debug.WriteLine("Not Added!");
            } 
            else
            {
                Debug.WriteLine("Success!");
            }
            return true;
        }
    }
}
