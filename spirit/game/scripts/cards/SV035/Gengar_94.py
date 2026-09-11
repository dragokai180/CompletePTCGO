from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='38f308e2-2988-5c0a-a740-edcc3cce43c0',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name',
    display_name='Gengar',
    searchable_by=['Gengar', 'Stage 2', 'Gengar'],
    subtypes=['Stage 2'],
    collector_number=94,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name',
    family_id=92,
    abilities=[
        Attack(
            title='Poltergeist',
            game_text='Your opponent reveals their hand. This attack does 50 damage for each Trainer card you find there.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Hollow Dive',
            game_text="Put 3 damage counters on your opponent's Benched Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
