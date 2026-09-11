from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='36742245-10fc-5a40-97d9-00513d066b6a',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name',
    display_name='Bastiodon',
    searchable_by=['Bastiodon', 'Stage 1', 'Bastiodon'],
    subtypes=['Stage 1'],
    collector_number=70,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name',
    family_id=410,
    abilities=[
        Attack(
            title='Counter Head',
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put damage counters on the Attacking Pokémon equal to the damage done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Fortress of Rage',
            game_text='This attack does 10 more damage for each of your Benched Pokémon that has any damage counters on it.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
