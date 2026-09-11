from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a96a396-bde5-5c0e-b8f0-fe1f8cc0785f',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name',
    display_name='Ampharos',
    searchable_by=['Ampharos', 'Stage 2', 'Prime', 'Ampharos'],
    subtypes=['Stage 2', 'Prime'],
    collector_number=105,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
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
            title='Conductivity',
            game_text='Whenever your opponent attaches an Energy card from his or her hand to 1 of his or her Pokémon, put 1 damage counter on that Pokémon.',
            ability_type=AbilityTypes.POKE_BODY,
            effect=standard_ability,
            trigger=Triggers.ON_ENERGY_ATTACHED,
        ),
        Attack(
            title='Lightning Crush',
            game_text='Flip a coin. If heads, this attack does 40 damage plus 40 more damage. If tails, discard an Energy attached to the Defending Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
