from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='790222fa-58ef-5b5b-9495-e44455e030af',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name',
    display_name='Roggenrola',
    searchable_by=['Roggenrola', 'Basic', 'Roggenrola'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=524,
    abilities=[
        Attack(
            title='Smack Down',
            game_text="If your opponent's Active Pokémon has Fighting Resistance, this attack does 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
