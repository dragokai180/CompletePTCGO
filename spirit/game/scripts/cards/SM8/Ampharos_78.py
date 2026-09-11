from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='db5ca5ed-986a-5ddb-98b8-050acd8a2727',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name',
    display_name='Ampharos',
    searchable_by=['Ampharos', 'Stage 2', 'Ampharos'],
    subtypes=['Stage 2'],
    collector_number=78,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
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
            title='Unseen Flash',
            game_text="Once during your turn (before your attack), you may put 2 Lightning Energy cards from your hand in the Lost Zone. If you do, your opponent's Active Pokémon is now Paralyzed.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Split Bomb',
            game_text="This attack does 50 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=standard_attack,
        ),
    ],
)
