from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab4f0380-d3ac-5433-a659-7312f4effe58',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name',
    display_name='Aegislash',
    searchable_by=['Aegislash', 'Stage 2', 'Aegislash'],
    subtypes=['Stage 2'],
    collector_number=95,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    family_id=679,
    abilities=[
        Ability(
            title='Durable Blade',
            game_text="If this Pokémon is Knocked Out by damage from an opponent's attack, put it into your hand instead of the discard pile. (Discard all cards attached to it.)",
            passive=standard_passive("If this Pokémon is Knocked Out by damage from an opponent's attack, put it into your hand instead of the discard pile. (Discard all cards attached to it.)"),
        ),
        Attack(
            title='Trash Slash',
            game_text="This attack does 10 damage for each Item card in your discard pile. You can't do more than 130 damage in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
