using System.Windows;
using static bazPlannerWPF.sqlite_connect;
using static bazPlannerWPF.Owner;
using System.Data.SQLite;

namespace bazPlannerWPF
{
    public partial class create_user : Window
    {
        static SQLiteCommand cmd;
       
        public create_user()
        {
            InitializeComponent();
        }

        private void Add_to_DB(object sender, RoutedEventArgs e)
        {
            Owner asd = new Owner
            {
                nameOwner = username.Text,
                passwordOwner = userpswd.Text
            };

            asd.AddToDatabase(asd.nameOwner, asd.passwordOwner);
        }
    }
}
