from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9b87e565-39e0-5235-b61d-f5a5e552b06f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name',
    display_name='Wugtrio',
    searchable_by=['Wugtrio', 'Stage 1', 'Wugtrio'],
    subtypes=['Stage 1'],
    collector_number=57,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name',
    family_id=960,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title='Undersea Tunnel',
            game_text="Flip 3 coins. For each heads, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
