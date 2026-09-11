from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6dfffb0c-7772-5349-bc80-548dc0f14fa2',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name',
    display_name='Raticate',
    searchable_by=['Raticate', 'Stage 1', 'Raticate'],
    subtypes=['Stage 1'],
    collector_number=88,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    family_id=19,
    abilities=[
        Ability(
            title='Antibodies',
            game_text="This Pokémon can't be affected by any Special Conditions. (Remove any Special Conditions affecting this Pokémon.)",
            passive=standard_passive("This Pokémon can't be affected by any Special Conditions. (Remove any Special Conditions affecting this Pokémon.)"),
        ),
        Attack(
            title='Dirty Shock',
            game_text="Your opponent's Active Pokémon is now Poisoned. Discard all Pokémon Tool cards attached to that Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
