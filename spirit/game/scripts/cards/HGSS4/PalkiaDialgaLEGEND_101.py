from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c91cdf74-5d4d-525a-954b-525f2ad8a152',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaDialgaLEGEND.Name',
    display_name='Palkia & Dialga LEGEND',
    searchable_by=['Palkia & Dialga LEGEND', 'LEGEND', 'PalkiaDialgaLEGEND'],
    subtypes=['LEGEND'],
    collector_number=101,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=160,
    elements=[PokemonTypes.WATER, PokemonTypes.METAL],
    stage=PokemonStage.LEGEND,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    weakness_types=[PokemonTypes.LIGHTNING, PokemonTypes.FIRE],
    family_id=483,
    abilities=[
        Attack(
            title='Sudden Delete',
            game_text="Choose 1 of your opponent's Benched Pokémon. Put that Pokémon and all cards attached to it back to your opponent's hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Time Control',
            game_text="Discard all Metal Energy attached to Palkia & Dialga LEGEND. Add the top 2 cards of your opponent's deck to his or her Prize cards.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
