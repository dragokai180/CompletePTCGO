from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a5a9b0ee-71b4-5eef-a4ae-470205221499',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seaking.Name',
    display_name='Seaking',
    searchable_by=['Seaking', 'Stage 1', 'Seaking'],
    subtypes=['Stage 1'],
    collector_number=119,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name',
    family_id=118,
    abilities=[
        Attack(
            title='Swim Freely',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Horn',
            game_text='This attack does 30 more damage for each Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
