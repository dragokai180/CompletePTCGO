from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc6b944c-d902-51e2-bf31-fae4b6d2c03e',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    display_name='Haunter',
    searchable_by=['Haunter', 'Stage 1', 'Haunter'],
    subtypes=['Stage 1'],
    collector_number=69,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name',
    family_id=92,
    abilities=[
        Attack(
            title='Sinister Fog',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 1 damage counter on each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
