from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='71d4698d-0498-5190-9885-3c93551368c4',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name',
    display_name='Magnezone',
    searchable_by=['Magnezone', 'Stage 2', 'Magnezone'],
    subtypes=['Stage 2'],
    collector_number=36,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name',
    family_id=81,
    abilities=[
        Ability(
            title='Magnetic Circuit',
            game_text='As often as you like during your turn (before your attack), you may attach a Lightning Energy card from your hand to 1 of your Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Zap Cannon',
            game_text="This Pokémon can't use Zap Cannon during your next turn.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
