from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='59398bbd-8dd7-5eed-892f-cdb27c1d2c2d',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name',
    display_name='Salazzle',
    searchable_by=['Salazzle', 'Stage 1', 'Salazzle'],
    subtypes=['Stage 1'],
    collector_number=16,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name',
    family_id=757,
    abilities=[
        Ability(
            title='Hot Poison',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may leave your opponent's Active Pokémon Burned and Poisoned.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
