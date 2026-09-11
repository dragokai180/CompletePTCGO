from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9badf67a-0551-54be-971d-faa62e67e2fe',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name',
    display_name='Spinarak',
    searchable_by=['Spinarak', 'Basic', 'Spinarak'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=167,
    abilities=[
        Attack(
            title='Hang Down',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Spider Web',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
