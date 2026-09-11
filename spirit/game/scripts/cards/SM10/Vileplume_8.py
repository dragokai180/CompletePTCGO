from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1146ebe4-4506-597e-95b8-67821ddf0b02',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name',
    display_name='Vileplume',
    searchable_by=['Vileplume', 'Stage 2', 'Vileplume'],
    subtypes=['Stage 2'],
    collector_number=8,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Ability(
            title='Varied Pollen',
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, choose Asleep, Burned, Confused, or Poisoned. Your opponent's Active Pokémon is now affected by that Special Condition.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Giant Bloom',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
