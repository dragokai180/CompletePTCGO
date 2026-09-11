from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ded4dde6-ed25-57cc-ae4b-63a801e5b562',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    display_name='Kirlia',
    searchable_by=['Kirlia', 'Stage 1', 'Kirlia'],
    subtypes=['Stage 1'],
    collector_number=81,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name',
    family_id=280,
    abilities=[
        Attack(
            title='Hypnosis',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spiral Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
