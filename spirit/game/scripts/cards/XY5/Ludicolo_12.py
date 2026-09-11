from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='73dbf764-cff7-56d8-8907-f5a6d3098b27',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name',
    display_name='Ludicolo',
    searchable_by=['Ludicolo', 'Stage 2', 'Ludicolo'],
    subtypes=['Stage 2'],
    collector_number=12,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name',
    family_id=270,
    abilities=[
        Ability(
            title='Captivating Rhythm',
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Solar Ray',
            game_text='Heal 20 damage from each of your Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
