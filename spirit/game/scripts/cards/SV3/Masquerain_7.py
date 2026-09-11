from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee3a3b34-5072-548b-a870-fa4256232163',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name',
    display_name='Masquerain',
    searchable_by=['Masquerain', 'Stage 1', 'Masquerain'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name',
    family_id=283,
    abilities=[
        Attack(
            title='Panic-Prompting Pattern',
            game_text="Flip a coin until you get tails. For each heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bug Buzz',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
