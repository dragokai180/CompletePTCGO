from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9eb384a6-56b5-5338-ad4a-ae64f6dac685',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name',
    display_name='Ampharos',
    searchable_by=['Ampharos', 'Stage 2', 'Ampharos'],
    subtypes=['Stage 2'],
    collector_number=40,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name',
    family_id=179,
    abilities=[
        Ability(
            title='Shocking Light',
            game_text="Once during your turn (before your attack), you may put 3 damage counters on 1 of your opponent's Pokémon-EX.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Gigavolt',
            game_text="Flip a coin. If heads, this attack does 40 more damage. If tails, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
