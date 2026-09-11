from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cbd25aef-0f15-5cf1-a8b5-ba974beb7f00',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Araquanid.Name',
    display_name='Araquanid',
    searchable_by=['Araquanid', 'Stage 1', 'Araquanid'],
    subtypes=['Stage 1'],
    collector_number=65,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name',
    family_id=751,
    abilities=[
        Attack(
            title='Headstrike',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title='Liquidation',
            game_text='During your next turn, the Defending Pokémon takes 60 more damage from attacks (after applying Weakness and Resistance).',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
