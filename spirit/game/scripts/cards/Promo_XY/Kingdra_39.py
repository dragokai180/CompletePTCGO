from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2f310d96-7827-540b-aa04-fba46495cd0d',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name',
    display_name='Kingdra',
    searchable_by=['Kingdra', 'Stage 2', 'Kingdra'],
    subtypes=['Stage 2'],
    collector_number=39,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    family_id=230,
    abilities=[
        Attack(
            title='Gather Strength',
            game_text='Search your deck for up to 4 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Blast',
            game_text='Discard a Water and a Lightning Energy attached to this Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.LIGHTNING: 1},
            damage=150,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('When you attach an Energy card from your hand to this Pokémon (except with an attack, Ability, or Trainer card), you may attach 2 Energy cards.'),
)
