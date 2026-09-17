from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0216a86c-ec90-579f-845b-3a512a356769',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name',
    display_name='Yanmega',
    searchable_by=['Yanmega', 'Stage 1', 'Yanmega'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name',
    family_id=193,
    abilities=[
        Ability(
            title='Sonic Vision',
            game_text="If you have exactly 4 cards in your hand, ignore all Energy in the attack cost of each of this Pokémon's attacks.",
            effect=standard_ability,
        ),
        Attack(
            title='Assault Boom',
            game_text="If your opponent's Active Pokémon has a Pokémon Tool card attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
