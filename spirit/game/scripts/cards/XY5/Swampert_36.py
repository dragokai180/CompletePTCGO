from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb2a8636-dec1-5754-89da-baa24c43b17e',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name',
    display_name='Swampert',
    searchable_by=['Swampert', 'Stage 2', 'Swampert'],
    subtypes=['Stage 2'],
    collector_number=36,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name',
    family_id=258,
    abilities=[
        Ability(
            title='Diving Search',
            game_text='Once during your turn (before your attack), you may search your deck for a card. Shuffle your deck, then put that card on top of it.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Hydro Pump',
            game_text='This attack does 30 more damage for each Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('When you attach an Energy card from your hand to this Pokémon (except with an attack, Ability, or Trainer card), you may attach 2 Energy cards.'),
)
