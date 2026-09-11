from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='25d6c811-c449-5d53-8cbd-33fb187cdaa1',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name',
    display_name='Herdier',
    searchable_by=['Herdier', 'Stage 1', 'Herdier'],
    subtypes=['Stage 1'],
    collector_number=175,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name',
    family_id=506,
    abilities=[
        Attack(
            title='Work Up',
            game_text="During your next turn, this Pokémon's attacks do 60 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
