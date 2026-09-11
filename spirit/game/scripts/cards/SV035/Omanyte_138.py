from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4234b267-1fa2-5565-885c-7886f8311aa3',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name',
    display_name='Omanyte',
    searchable_by=['Omanyte', 'Stage 1', 'Omanyte'],
    subtypes=['Stage 1'],
    collector_number=138,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AntiqueHelixFossil.Name',
    family_id=138,
    abilities=[
        Attack(
            title='Tentacular Return',
            game_text="Put an Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
