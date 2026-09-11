from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='175b5dfa-ad52-5915-aaf9-51dec39249f4',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name',
    display_name='Floatzel',
    searchable_by=['Floatzel', 'Stage 1', 'Floatzel'],
    subtypes=['Stage 1'],
    collector_number=36,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    family_id=418,
    abilities=[
        Attack(
            title='Agility',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Blast',
            game_text='Discard a Water Energy from this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
