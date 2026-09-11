from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='122c7698-8422-5d01-9de8-cc9519fd9966',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name',
    display_name='Chandelure',
    searchable_by=['Chandelure', 'Stage 2', 'Chandelure'],
    subtypes=['Stage 2'],
    collector_number=38,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name',
    family_id=607,
    abilities=[
        Attack(
            title='Combustion Chain',
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
        ),
    ],
)
