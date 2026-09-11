from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='acfd9d39-07ab-5d7d-91ee-cb8753fe0fc7',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    display_name='Kirlia',
    searchable_by=['Kirlia', 'Stage 1', 'Kirlia'],
    subtypes=['Stage 1'],
    collector_number=140,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name',
    family_id=280,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Disarming Voice',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
