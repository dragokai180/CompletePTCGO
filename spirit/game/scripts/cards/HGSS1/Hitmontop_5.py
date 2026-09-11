from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cea5d8d0-ece0-57ca-a929-8af333d6cc52',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name',
    display_name='Hitmontop',
    searchable_by=['Hitmontop', 'Basic', 'Hitmontop'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=237,
    abilities=[
        Attack(
            title='Triple Kick',
            game_text='Flip 3 coins. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Close Combat',
            game_text="During your opponent's next turn, any damage done to Hitmontop by attacks is increased by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
