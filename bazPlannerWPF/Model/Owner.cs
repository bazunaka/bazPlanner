using System.Windows;
using System.Data.SQLite;
using static bazPlannerWPF.DBConnect;

namespace bazPlannerWPF
{
    public class Owner
    {
        public string nameOwner = default;
        public string passwordOwner = default;
        static public string nameAuth = default;

        public void AddToDatabase(string nameOwner, string passwordOwner)
        {
            InsertUser(nameOwner, passwordOwner);
        }
        static public void CheckAdmin()
        {

        }

        static public string Auth(string nameOwner, string passwordOwner)
        {  
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT * FROM owner WHERE name_owner='{nameOwner}' AND password_owner='{passwordOwner}'"
            };
            SQLiteDataReader reader = command.ExecuteReader();
            if (reader.HasRows)
            {
                ((MainWindow)Application.Current.MainWindow).menuCreateProject.IsEnabled = true;
                ((MainWindow)Application.Current.MainWindow).menuCreateTask.IsEnabled = true;
                nameAuth = nameOwner;
                return nameAuth;
            }
            else
            {
                return "Not register!";
            }            
        }
    }
}
