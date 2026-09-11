from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee50649b-e6cf-5571-9a58-db294e4631d8',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krookodile.Name',
    display_name='Krookodile',
    searchable_by=['Krookodile', 'Stage 2', 'Krookodile'],
    subtypes=['Stage 2'],
    collector_number=71,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name',
    family_id=551,
    abilities=[
        Attack(
            title='Bother',
            game_text="Flip a coin. If heads, your opponent can't play any Supporter cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Knock Back',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
