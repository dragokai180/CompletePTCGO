from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f461478d-3536-599b-93a9-6272e665b66a',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name',
    display_name='Raticate',
    searchable_by=['Raticate', 'Stage 1', 'Raticate'],
    subtypes=['Stage 1'],
    collector_number=67,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    family_id=19,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Shadowy Bite',
            game_text="This attack does 60 damage times the number of Special Energy cards in your opponent's discard pile.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
