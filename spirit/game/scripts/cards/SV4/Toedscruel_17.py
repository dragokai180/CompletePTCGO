from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3d21d83-eeda-50a8-bd25-46b2b76d5175',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruel.Name',
    display_name='Toedscruel',
    searchable_by=['Toedscruel', 'Stage 1', 'Toedscruel'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name',
    family_id=948,
    abilities=[
        Ability(
            title='Slime Mold Colony',
            game_text="Cards in your opponent's discard pile can't be put into their hand by an effect of your opponent's Abilities or Trainer cards.",
            passive=standard_passive("Cards in your opponent's discard pile can't be put into their hand by an effect of your opponent's Abilities or Trainer cards."),
        ),
        Attack(
            title='Mushroom Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
