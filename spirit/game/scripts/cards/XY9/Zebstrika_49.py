from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='18d45e1c-a8b1-5888-8a77-8c96b75405b3',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name',
    display_name='Zebstrika',
    searchable_by=['Zebstrika', 'Stage 1', 'Zebstrika'],
    subtypes=['Stage 1'],
    collector_number=49,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name',
    family_id=522,
    abilities=[
        Ability(
            title='Zap Zone',
            game_text="Damage from the attacks of your Lightning Pokémon isn't affected by any effects on your opponent's Active Pokémon.",
            passive=standard_passive("Damage from the attacks of your Lightning Pokémon isn't affected by any effects on your opponent's Active Pokémon."),
        ),
        Attack(
            title='Crashing Bolt',
            game_text="If your opponent's Active Pokémon has Fighting Resistance, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
