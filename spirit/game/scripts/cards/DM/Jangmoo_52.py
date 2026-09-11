from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9cdbf3db-08ce-5308-bf74-b00b8c9100d1',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name',
    display_name='Jangmo-o',
    searchable_by=['Jangmo-o', 'Basic', 'Jangmoo'],
    subtypes=['Basic'],
    collector_number=52,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=782,
    abilities=[
        Attack(
            title='Rigidify',
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
