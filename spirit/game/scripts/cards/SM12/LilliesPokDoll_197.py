from spirit.game.data_utils import Ability, Activations, FossilItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_passive,
)


_TEXT = "Play this card as if it were a 30-HP Colorless Basic Pokémon. At any time during your turn (before your attack), if this Pokémon is your Active Pokémon, you may discard all cards from it and put it on the bottom of your deck. This card can't retreat. If this card is Knocked Out, your opponent can't take any Prize cards for it. You may play as many Item cards as you like during your turn (before your attack)."

card = FossilItemCardDef(
    guid='048b0ead-88e2-50e4-a3bd-39fe77e426f6',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LilliesPokDoll.Name',
    display_name="Lillie's Poké Doll",
    searchable_by=["Lillie's Poké Doll", 'Item', 'LilliesPokDoll'],
    subtypes=['Item'],
    collector_number=197,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=30,
    passive=standard_passive(_TEXT),
    abilities=[Ability(
        title="Put Lillie's Poké Doll Away",
        game_text=_TEXT,
        effect=standard_ability,
        activation=Activations.UNLIMITED,
        condition=lambda board, player_id, source=None: (
            source is not None and board.active_pokemon(player_id) is source
        ),
    )],
)
