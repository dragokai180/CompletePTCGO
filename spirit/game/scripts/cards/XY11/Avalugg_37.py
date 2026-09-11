from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c7117bd-63c8-551d-852d-f0af0732b491',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Avalugg.Name',
    display_name='Avalugg',
    searchable_by=['Avalugg', 'Stage 1', 'Avalugg'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name',
    family_id=712,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Melting Floe',
            game_text="Discard the top 3 cards of your deck. For each Water Energy card you discarded in this way, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.WATER: 3},
            effect=standard_attack,
        ),
    ],
)
