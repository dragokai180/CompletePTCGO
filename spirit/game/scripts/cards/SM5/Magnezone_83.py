from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2db45f46-7f37-5c0f-9c67-83142fbe17d9',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name',
    display_name='Magnezone',
    searchable_by=['Magnezone', 'Stage 2', 'Magnezone'],
    subtypes=['Stage 2'],
    collector_number=83,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name',
    family_id=81,
    abilities=[
        Ability(
            title='Magnetic Circuit',
            game_text='As often as you like during your turn (before your attack), you may attach a Metal Energy card from your hand to 1 of your Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Zap Cannon',
            game_text="This Pokémon can't use Zap Cannon during your next turn.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
