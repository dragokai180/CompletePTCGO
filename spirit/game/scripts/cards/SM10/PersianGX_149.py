from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6a9444c9-e2c0-5547-bedd-4362f9437b4f',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PersianGX.Name',
    display_name='Persian-GX',
    searchable_by=['Persian-GX', 'Stage 1', 'GX', 'PersianGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=149,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    family_id=52,
    abilities=[
        Ability(
            title='Cat Walk',
            game_text="Once during your turn (before your attack), if 1 of your Pokémon-GX or Pokémon-EX was Knocked Out during your opponent's last turn, you may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck. You can't use more than 1 Cat Walk Ability each turn.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Vengeance',
            game_text="This attack does 20 more damage for each Pokémon in your discard pile. You can't add more than 180 damage in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Slash Back-GX',
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
