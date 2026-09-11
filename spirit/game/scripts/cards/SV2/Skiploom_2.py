from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='892a6dbf-4c94-5f81-825c-a2581637b260',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name',
    display_name='Skiploom',
    searchable_by=['Skiploom', 'Stage 1', 'Skiploom'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name',
    family_id=187,
    abilities=[
        Ability(
            title='Drifting Dodge',
            game_text='If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.',
            passive=standard_passive('If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.'),
        ),
        Attack(
            title='Flowery Zephyr',
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
