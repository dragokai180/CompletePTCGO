from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='488ecf73-f09a-57d4-ae67-9ec066125778',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name',
    display_name='Delcatty',
    searchable_by=['Delcatty', 'Stage 1', 'Delcatty'],
    subtypes=['Stage 1'],
    collector_number=132,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name',
    family_id=301,
    abilities=[
        Ability(
            title='Search for Friends',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put 2 Supporter cards from your discard pile into your hand.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Cat Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
