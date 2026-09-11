from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba612f63-9872-5ac4-960f-408112565439',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jumpluff.Name',
    display_name='Jumpluff',
    searchable_by=['Jumpluff', 'Stage 2', 'Jumpluff'],
    subtypes=['Stage 2'],
    collector_number=3,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name',
    family_id=187,
    abilities=[
        Ability(
            title='Drifting Dodge',
            game_text='If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.',
            passive=standard_passive('If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.'),
        ),
        Attack(
            title='Fluffy Breeze',
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
