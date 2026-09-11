from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0aec7096-b326-5be3-ac9d-d49b12759d36',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name',
    display_name='Tarountula',
    searchable_by=['Tarountula', 'Basic', 'Tarountula'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=917,
    abilities=[
        Attack(
            title='Bind Down',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
