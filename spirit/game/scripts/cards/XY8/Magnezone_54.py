from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1c753de-5dea-5afe-a995-ba08ebcdca4c',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name',
    display_name='Magnezone',
    searchable_by=['Magnezone', 'Stage 2', 'Magnezone'],
    subtypes=['Stage 2'],
    collector_number=54,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
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
            title='Thunder Blast',
            game_text='Discard a Lightning Energy attached to this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
