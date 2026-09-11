from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c0e4b6b3-102e-581c-8794-b700bd5f0329',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name',
    display_name='Wailord',
    searchable_by=['Wailord', 'Stage 1', 'Wailord'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name',
    family_id=320,
    abilities=[
        Attack(
            title='Dive',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Open Sea',
            game_text='Heal 30 damage from each of your Water Pokémon.',
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
