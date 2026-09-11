from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fb3dea45-2a49-5a9f-b3b2-94303853429d',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name',
    display_name='Tsareena',
    searchable_by=['Tsareena', 'Stage 2', 'Tsareena'],
    subtypes=['Stage 2'],
    collector_number=20,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name',
    family_id=761,
    abilities=[
        Ability(
            title='Queenly Majesty',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may have your opponent reveal their hand. Then, discard a card from it.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Trop Kick',
            game_text='Heal 20 damage and remove all Special Conditions from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
