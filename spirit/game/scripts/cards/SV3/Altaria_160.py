from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a0e0247b-f156-5a79-b3fe-f41ad9f71ba8',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name',
    display_name='Altaria',
    searchable_by=['Altaria', 'Stage 1', 'Altaria'],
    subtypes=['Stage 1'],
    collector_number=160,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    family_id=333,
    abilities=[
        Attack(
            title='Glide',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Soothing Lullaby',
            game_text="Your opponent's Active Pokémon is now Asleep. During Pokémon Checkup, your opponent flips 2 coins instead of 1. If either of them is tails, that Pokémon is still Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.METAL: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
